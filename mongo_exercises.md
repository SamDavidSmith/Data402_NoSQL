### Question 5

1. Find Luke Skywalker: <br>
`db.characters.find({name: "Luke Skywalker"})`
2. Find Chewbacca and list name and eye colour:<br>
`db.characters.find({name: "Chewbacca"}, {name: 1, eye_color: 1})`
3. Check the species name of Ackbar: <br>
`db.characters.find({name: "Ackbar"}, {"species.name": 1})`

### Question 6:

1. Find the names and homeworld names for humans in the collection: <br>
`db.characters.find({"species.name": "Human"}, {name: 1, "homeworld.name": 1})`

### Question 7:

1. Find all entries that have a yellow or orange eye colour:
`db.characters.find({eye_color: { $in: ["yellow", "orange"]}})`

### Question 8:

1. Filter characters for entities that have blue eyes and are females:
```mongosh
db.characters.find({ 
$and: [
  {eye_color: "blue"},
  {gender: "female"}
  ]
  })
```
2. Filter characters that have blue eyes or are females:
```mongosh
db.characters.find({ 
$or: [
  {eye_color: "blue"},
  {gender: "female"}
  ]
  })
```
### Question 9:

1. Filter characters that have a height greater than 200: <br>
`db.characters.find( { height: { $gt: 200 } }, {name: 1, height: 1} )`
2. Convert "unknown" to null values: <br>
`db.characters.updateMany(
    { height: "unknown" },
    { $set: { "height": null } })`
3. Convert to integers:
```
db.characters.updateMany(
    {},
    [
    {$set: {height: { $toInt: "$height" }}}
    ]
)
```
The square brackets ensure that an aggregate function that converts all the height strings to integers with $toInt is called.