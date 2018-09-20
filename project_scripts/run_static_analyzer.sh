#!/bin/bash

cd ..

pylint --load-plugins pylint_django [..other options..] tasks --disable=missing-docstring | tee project_scripts/static_analyzer_output/static_analyzer_tasks.txt

pylint --load-plugins pylint_django [..other options..] e2etests --disable=missing-docstring | tee project_scripts/static_analyzer_output/static_analyzer_e2etests.txt
