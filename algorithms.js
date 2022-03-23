// <-------------TwoSum LEETCODE#1--------------->

const twoSum = (arr, target) => {
  // create a hashtable to store the nums
  let nums = {};
  for (let i = 0; i < arr.length; i++) {  // for loop through the nums
    const currNum = arr[i]; //initialize the current number we are at
    const possiblePair = target - currNum; // if you find the difference of the current number and the target
    if (possiblePair in nums) {  // result difference of target - currNum is not in the hashmap then we keep on iterating
      return [i, nums[possiblePair]]; // return the number we are at and the result of target - the currNum
    } else {
      nums[currNum] = i;
    }
  }
}

// <-------------FlattenArray META-PREP--------------->

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

// <-------------Best Time to Buy and Sell Stock LEETCODE #121--------------->

const maxProfit = (pricesArr) => {
  let maxProfit = 0;   // initalize a max profit variable
  let minPrice = pricesArr[0]; // initalize a minPrice variable to keep track of a lower price that may come up in the prices array
  for (const price of pricesArr) {
    const currProfit = price - minPrice; // intializing a current profit variable to keep track of the best profit margin
    if (currProfit > maxProfit) { // if the current profit is greater than our current max profit
      maxProfit = currProfit; //we assign current profit to max profit
    } else if (price < minPrice) { // if current profit is not greater than our maxprofit 
      minPrice = price; // we can assign the price we are at to minPrice
    }
  }
  return maxProfit;
}

// <-------------Contains Duplicate LEETCODE #217--------------->

const constainsDuplicate = (numsArr) => {
  const numsSet = new Set(); // create a nums set
  for (const num of numsArr) { // for loop through the numbers
    if (numsSet.has(num)) { // check to see if the nums set has already the number you are currently on inside of the loop
      return true;   // return true if it does
    }
    numsSet.add(num); // if not then we just add it to the hashset
  }
  return false; // outside of the loop we can return false because we did not find a duplicate
}

// <-------------Maximum Subarray LEETCODE #53--------------->
let arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

const maxSubArray = (nums) => {

}

// maxSubArray(arr);