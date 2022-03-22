// <-------------FlattenArray--------------->

let exampleArray = [1,2,[3,4,5], [4]];
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