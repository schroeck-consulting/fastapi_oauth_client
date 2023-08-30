#!/bin/sh
source ./example.env
uvicorn example:app --reload
