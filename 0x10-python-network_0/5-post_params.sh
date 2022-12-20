#!/bin/bash
# sends a POST request to the passed URL,A variable email must be sent with the value test@gmail.com with the value I will always be here for PLD
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
