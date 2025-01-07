#!/usr/bin/bash
# Commands for setting up django 
clear

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[0;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[0;37m'
export NC='\033[0m' # No Color

# Commands
b1() {
    echo -e "${CYAN} ======================"
    echo -e "Commands for setting up django"
    echo -e "New django project - uv run django-admin startproject mypanty"
    echo -e "Run server - uv run python manage.py runserver"
    echo -e " ======================${NC}"
}

c1() {
    echo -e "${GREEN} hi"
}

# Execution
b1
