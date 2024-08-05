REMOTE_URL="https://$LT_USERNAME:$LT_ACCESS_KEY@hub.lambdatest.com/wd/hub"


FILTER="src/tests/test_lambdatest.py -k test_google_lambda_test"

python -m pytest $FILTER --remote-url=$REMOTE_URL