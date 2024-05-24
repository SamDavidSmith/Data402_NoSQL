### Question 5

1. Find Luke Skywalker: <br>
`db.characters.find({name: "Luke Skywalker"})`
2. Find Chewbacca and list name and eye colour:<br>
`db.characters.find({name: "Chewbacca"}, {name: 1, eye_color: 1})`
   * The binary notation means you write 1 for the columns you want to show, and 0 for those you want to hide.
3. Check the species name of Ackbar: <br>
`db.characters.find({name: "Ackbar"}, {"species.name": 1})`
   * The dot accesses sub-fields inside embedded values (putting key-value pairs as values).

### Question 6:

1. Find the names and homeworld names for humans in the collection: <br>
`db.characters.find({"species.name": "Human"}, {name: 1, "homeworld.name": 1})`

### Question 7:

1. Find all entries that have a yellow or orange eye colour:
`db.characters.find({eye_color: { $in: ["yellow", "orange"]}})`
   * Using $in with an array means you are searching for entities with values in that array.

### Question 8:

1. Filter characters for entities that have blue eyes and are females:
```mongosh
db.characters.find({ 
$and: [
  {eye_color: "blue"},
  {gender: "female"}
  ]
  } 
  {name: 1, eye_color: 1, gender: 1})
```
*   Just like $in, you have $and along with an array, which searches for rows that include all of the values in the array.

2. Filter characters that have blue eyes or are females:
```mongosh
db.characters.find({ 
$or: [
  {eye_color: "blue"},
  {gender: "female"}
  ]
  }, 
  {name: 1, eye_color: 1, gender: 1})
```
*   $or ensures at least one of the values in the array are met.
### Question 9:

1. Filter characters that have a height greater than 200: <br>
`db.characters.find( { height: { $gt: 200 } }, {name: 1, height: 1} )`
   * $gt, the aggregation function for >, doesn't require a []
2. Convert "unknown" to null values: <br>
`db.characters.updateMany(
    { height: "unknown" },
    { $set: { "height": null } })`
   * Here I am finding all the entities with height as a string "unknown", and then using $set to put the height value in these entities as null.
3. Convert to integers:
```
db.characters.updateMany(
    {},
    [
    {$set: {height: { $toInt: "$height" }}}
    ]
)
```
Here, I am finding every entity in the collection with {}, and because the function $toInt is being used to collect an entire height column of integers, the [] surround the column to produce an array, which is then updated into the documents.

### Other Functions:
* **$eq**: returns True if the two values are equal: <br>
`qtyEq250: { $eq: [ "$qty", 250 ] }` returns True if the values inside the array are the same. <br>
<br>
* **$gte**: Returns True if the right value is greater than or equal to the left value: <br>
`qtyGte250: { $gte: [ "$qty", 250 ] }` returns
```mongosh
{ "item" : "abc1", "qty" : 300, "qtyGte250" : true }
{ "item" : "abc2", "qty" : 200, "qtyGte250" : false }
{ "item" : "xyz1", "qty" : 250, "qtyGte250" : true }
{ "item" : "VWZ1", "qty" : 300, "qtyGte250" : true }
{ "item" : "VWZ2", "qty" : 180, "qtyGte250" : false }
```

* **$lt** and **$lte** are 'less than' and 'less than or equal to': <br>
`qtyLt250: { $lt: [ "$qty", 250 ] }` & `qtyLte250: { $lte: [ "$qty", 250 ] }`
<br> <br>
* **$ne** returns True for when the two values in the array are not equal: <br>
`qtyNe250: { $ne: [ "$qty", 250 ] }` returns
```
{ "item" : "abc2", "qty" : 200, "qtyNe250" : true }
{ "item" : "xyz1", "qty" : 250, "qtyNe250" : false }
```
* **$nin**: the opposite of $in above: <br>
`db.characters.find({ mass : {$nin: []}})` finds the documents for which mass is not an empty string.

## Advanced MongoDB exercises:

### Exercise 1:
1. Write a query that finds the total (sum) of the height of all human characters in the db
```mongosh
db.characters.aggregate( [
   {$match: { "species.name": "Human" }},
   {$group: { _id: null, totalHeight: { $sum: "$height" } }}
] ).pretty()
```
2.Write a query that finds the max height per homeworld

```mongosh
db.characters.aggregate( [
   {$group: { _id: "$homeworld.name", totalHeight: { $sum: "$height" } }},
   {$sort: { _id: 1 }}
] )
```
3.Write a query that finds the mass and count per species. Filter out null values and sort by average mass (ascending order)

```mongosh
db.characters.aggregate( [
   {$match: { "species.name" : {$nin: [null]}, "mass" : {$nin: [null]}}},
   {$group: { _id: "$species.name", avgMass: { $avg: "$mass" }, count: { $sum: 1 } }},
   {$sort: { avgMass: 1 }}
] )
```

### Exercise 2:
1.Use .distinct() to find a list of all species names in the database

```mongosh
db.characters.distinct("species.name")
```
2.Use .count() or .countDocuments() to get a count of the amount of humans in the database

```mongosh
db.characters.countDocuments({"species.name": "Human"})
```
3. What does .estimatedDocumentCount({}) do?
```mongosh
db.orders.estimatedDocumentCount({})
```
This function does not take a filter, but rather counts all the documents in a collection.

### Exercise 3:

* Find Darth Vader's ObjectID:
```mongosh
db.characters.find({"name": "Darth Vader"}, {"_id": 1})
```
Output: _id: ObjectId('664e15999668b964a0d49f03')

```mongosh
db.starships.insertOne({
  name: "Millennium Falcon",
  model: "Heavily modified YT-1300fp light freighter",
  manufacturer: "Corellian Engineering Corporation",
  length: 34.63,
  max_atmosphering_speed: 1200,
  crew: 4,
  passengers: 6,
  pilot: []
})
```
```mongosh
db.starships.updateOne(
    { name: "Millennium Falcon" },
    { $set: { "pilot": [ObjectId("664e15a9ef9160c68b4b28bd"), ObjectId("664e1596d4f523bd5fc3310f"), ObjectId("664e15a163e4288969721cb6"), ObjectId("664e15b99f9549b28b267797")]} }
);

```