#!/bin/bash

poetry run pytest tests/performance_tests --benchmark-disable-gc --benchmark-min-rounds=1
