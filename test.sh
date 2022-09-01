# clear out the circle and person txt files
echo ""
bash LocalTests/run_person.sh
echo ""
bash LocalTests/run_circle.sh
echo ""
rm LocalTests/outputs/circle_test_output.txt
rm LocalTests/outputs/person_test_output.txt