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
    return i +1;
}

countUniqueValues([-2, -1, -1, 0, 1]);

