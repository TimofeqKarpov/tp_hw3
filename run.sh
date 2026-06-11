#!/usr/bin/env bash

case "$1" in
    "run_generator")
        docker run --rm -v "$(pwd)/data:/data" generator
        ;;
    "build_generator")
        docker build -t generator ./generator
        ;;
    "build_reporter")
        docker build -t reporter ./reporter
        ;;
    "run_reporter")
        docker run --rm -v "$(pwd)/data:/data" reporter
        ;;
    "create_local_data")
        python3 generator/generate.py local_data
        echo "Локальные данные созданны"
        ;;
    *)
        echo "Неизвестная команда"
        ;;
esac