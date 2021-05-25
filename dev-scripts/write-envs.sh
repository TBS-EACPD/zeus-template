set -a # automatically export all variables
source .env
set +a

[[ "$USE_DEV_SETTINGS" == "true" ]] || { 
    echo >&2 "ERROR: must use development .env file";
    # return 1; 
    exit
}
