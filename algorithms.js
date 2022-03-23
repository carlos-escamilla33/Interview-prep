// <-------------TwoSum LeetCode#1--------------->
const twoSum = (arr, target) => {
  // create a hashtable to store the nums
  let nums = {};
  for (let i = 0; i < arr.length; i++) {  // for loop through the nums
    const currNum = arr[i]; //initialize the current number we are at
    const possiblePair = target - currNum; // if you find the difference of the current number and the target
    if (possiblePair in nums) {  // if the result of target - currNum is not in the hashmap then we keep on iterating
      return [i, nums[possiblePair]]; // return the number we are at and the result of target - the currNum
    } else {
      nums[currNum] = i;
    }
  }
}

console.log(twoSum([3,2,4], 6));



// <-------------FlattenArray--------------->

let exampleArray = [1, 2, [3, 4, 5], [4]];
// let exampleArray = [1,2,[3,4,5,[6,7]]];
const flatten = (arr) => {
  let flatArray = []; // initalize empty array to push non array elements into
  for (let i = 0; i < arr.length; i++) { // for loop through the array
    const item = arr[i]; // initialize as item each element in the array
    if (Array.isArray(item)) { // check to see if the item is an array
      flatArray = flatArray.concat(flatten(item)); // if it is an array then we use recursion to break it down
      // we concat our current flat array to the returned value of the flattened array item
    } else {
      flatArray.push(item); // if the item is not an array then we simply push it to the flattened array
    }
  }
  return flatArray;
}

// console.log(flatten(exampleArray));

// <-------------Maximum Subarray LEETCODE #53--------------->
let arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

const maxSubArray = (nums) => {
  
}

// maxSubArray(arr);