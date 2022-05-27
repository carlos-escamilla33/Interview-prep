// <-------------Longest Substring Without Repeating CharactersLEETCODE #3--------------->

const lengthOfLongestSubstring = (str) => {
    let resultStr = "";
    let tempStr = "";
    let i = 0;
    let j = 0;
    while (i < str.length && j < str.length) {
        if (tempStr.indexOf(str[j]) === -1) {
            tempStr+=str[j];
            j++;
        } else {
            tempStr = "";
            i = i + 1;
            j = i;
        }
        if (tempStr.length > resultStr.length) {
            resultStr = tempStr;
        }
    }
    return resultStr.length;
}
