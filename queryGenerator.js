var randomWords = require("random-words");
const csv = require("csv-parser");
const fs = require("fs");
const createCsvWriter = require("csv-writer").createObjectCsvWriter;
const csvWriter = createCsvWriter({
  path: "out.csv",
  header: [
    { id: "sentence", title: "Sentence" },
    { id: "label", title: "Label" },
  ],
});

const hashQuery = []
let generatedRandomQuery = [];
const data = [];
 fs.createReadStream("hashQuery.csv")
  .pipe(csv())
  .on("data", (queryFormat) => {
    // console.log(queryFormat.SQL)
    hashQuery.push(queryFormat.SQL);
    // console.log(hashQuery)
  })
   .on("end", () => {
    //  console.log(hashQuery)
     let re = /#/gi;
     
     for (let i = 0; i < hashQuery.length; i++) {
      //  console.log(hashQuery[i]);
       generatedRandomQuery = hashQuery[i].replace(re, () => {
         return randomWords();
       });
      //  console.log(i, generatedRandomQuery);
       data.push({
         sentence: generatedRandomQuery,
         label: "0",
       });
     }
    //  console.log(data);
     
      csvWriter
        .writeRecords(data)
        .then(() => console.log("The CSV file was written successfully"));
    console.log("CSV file successfully processed");
  });










