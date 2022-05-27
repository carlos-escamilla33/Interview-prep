// <-------------Valid Anagram (Frequency Counter Algo)--------------->
const frequencyCounter = (word) => {
    let frequencyCounter = {};
    for (const letter of word) {
        if (!(letter in frequencyCounter)) {
            frequencyCounter[letter] = 1;
        }
        frequencyCounter[letter]++;
    }

    return frequencyCounter;
}

const validAnagram = (str1, str2) => {

    if (str1.length !== str2.length) return false;

    const strObj1 = frequencyCounter(str1);
    const strObj2 = frequencyCounter(str2);

    for (const letter in strObj1) {
        if (strObj2[letter] !== strObj1[letter]) {
            return false;
        }
    }

    return true;
}

// <-------------countUniqueValues--------------->
const countUniqueValues = (nums) => {
    let i = 0;
    for (let j = 1; j < nums.length; j++) {
        if (nums[i] !== nums[j]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}

// <-------------Frequency Counter - sameFrequency--------------->

const sameFrequency = (num1, num2) => {
    let strNum1 = num1.toString();
    let strNum2 = num2.toString();
    if (strNum1.length !== strNum2.length) return false;
    let numsObj = {};
    for (let i = 0; i < strNum1.length; i++) {
        numsObj[strNum1[i]] ? 
        numsObj[strNum1[i]]++ : numsObj[strNum1[i]] = 1
        numsObj[strNum2[i]] ? 
        numsObj[strNum2[i]]++ : numsObj[strNum2[i]] = 1
    }
    
    for (const num in numsObj) {
        const value = numsObj[num];
        if (value % 2 !== 0) {
            return false;
        }
    }
    return true;
}

// <-------------Frequency Counter/Multiple Pointers - areThereDuplicates--------------->

const areThereDuplicates = (...args) => {
    const arr = [...args];
    const freqCount = {};
    for (const el of arr) {
        freqCount[el] ? freqCount[el]++ : freqCount[el] = 1;
    }
    for (const key in freqCount) {
        if (freqCount[key] % 2 === 0) {
            return true;
        }
    }
    return false;
}

// <-------------Multiple Pointers - average Pair--------------->

const averagePair = (nums, target) => {
    // array is sorted we can use binary search to find the pair
    if (nums.length === 0) return false;
    let start = 0;
    let end = nums.length - 1;
    while (start < end) {
        const currSum = (nums[start] + nums[end]) / 2;
        if (currSum === target) {
            return true;
        } else if (currSum < target) {
            start++;
        } else if (currSum > target) {
            end--;
        }
    }
    return false;
}

// <-------------Multiple Pointers - isSubsequence--------------->

const isSubsequence = (str1, str2) => {
    let length = 0;
    let idx = 0;
    for (let i = 0; i < str2.length; i++) {
        if (str2[i] === str1[idx]) {
            length++;
            idx++;
        }
    }
    return length === str1.length;
}

// <-------------Sliding Window - maxSubarraySum--------------->

const maxSubArraySum = (arr, k) => {

    if (arr.length < k) return null; 

    let max = 0;
    let tempMax = 0;
    for (let i = 0; i < k; i++) {
        max+=arr[i];
    }
    tempMax = max;
    for (let i = k; i < arr.length; i++) {
        tempMax = tempMax + arr[i] - arr[i - k];
        max =  Math.max(max, tempMax);
    }

    return max;
}

// <-------------Sliding Window - minSubArrayLen--------------->

const minSubArrayLen = (arr, int) => {
    let resArr = [];
    let runningSum = 0;
    for (const num of arr) {
        if (num >= int) {
            resArr.push(num);
            runningSum+=num;
        }
    }
    

    return resArr.length;
}