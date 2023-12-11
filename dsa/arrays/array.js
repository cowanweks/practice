/*


*/

var marks = [40, 80, 50, 90, 20]

var fruits = [
    "Mangoes",
    "Oranges",
    "Avocados",
    "Bananas"
];

for (mark = 0; mark < marks.length; mark++)
    console.log(`${marks[mark]}`)

console.log("\n")

for (fruit = 0; fruit < fruits.length; fruit++)
    console.log(`${fruits[fruit]}`)

console.log("\n")


// Array methods in JavaScript

console.log("\n**Map**")
fruits.map((fruit) => {
    console.log(fruit)
})


fruits.push("Watermelon")
var filtered = fruits.filter((element) => element == 'Mangoes')

console.log("\n**Filtered data**\n", filtered)

console.log("\n**ForEach**")
fruits.forEach(fruit => { console.log(fruit) })
