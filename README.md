# counting-sort
Working –
Step 1 – Take input array & range(no of unique integer values involved)
Step 2 – Create the output array of size same as input array. Create count array with size equal to the range & initialize values to 0.
Step 3 – Count each element in the input array and place the count at the appropriate index of the count array
Step 4 – Modify the count array by adding the previous counts(cumulative). The modified count array indicates the position of each object/element in the output array.
Step 5 – Output each object from the input array into the sorted output array followed by decreasing its count by 1.
Step 6 – Print the sorted output array.
