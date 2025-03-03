#!/bin/bash

show_help() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h          Display this help message"
    echo "  -o FILE     Save the 'ics' content to the specified FILE"
    exit 0
}

BASE_URL="https://www.ai-cal.xyz"

output_file=""
while getopts "ho:" opt; do
    case ${opt} in
        h)
            show_help
            ;;
        o)
            output_file=$OPTARG
            ;;
        *)
            show_help
            ;;
    esac
done
shift $((OPTIND -1))

if [ $# -gt 0 ]; then
    prompt="$*"
elif [ ! -t 0 ]; then
    prompt=$(cat)
else
    echo "Enter your prompt (^C to cancel, ^D to send):"
    prompt=$(cat)
fi

if [ -z "$prompt" ]; then
    echo "Error: No prompt provided."
    exit 1
fi

prompt=$(echo "$prompt" | sed ':a;N;$!ba;s/\n/\\n/g')
escaped_prompt=$(echo "$prompt" | jq -Rs .)
json_payload="{\"prompt\": $escaped_prompt}"

response=$(curl -s -w "\n%{http_code}" -X POST "${BASE_URL}/api/parse" \
    -H "Content-Type: application/json" \
    -d "$json_payload")

http_status=$(echo "$response" | tail -n1)

response_body=$(echo "$response" | sed '$d')

if [ "$http_status" -ne 200 ]; then
    error_message=$(echo "$response_body" | jq -r '.detail // .error // "An unknown error occurred."')
    echo "Error: $error_message"
    exit 1
fi

ics_content=$(echo "$response_body" | jq -r '.ics')

if [ "$ics_content" == "null" ]; then
    echo "Error: 'ics' content not found in the response."
    exit 1
fi

if [ -n "$output_file" ]; then
    echo "$ics_content" > "$output_file"
    echo "'ics' content saved to $output_file"
else
    echo "$ics_content"
fi
