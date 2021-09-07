var randomWords = require("random-words");

const queryFormat = "SELECT * FROM # WHERE  # = '#'  AND City= '#' ";

let re = /#/gi;

let generatedRandomQuery = queryFormat.replace(re, () => {
  // console.log({ match });
  return randomWords();
});

console.log(generatedRandomQuery);


const createCsvWriter = require("csv-writer").createObjectCsvWriter;
const csvWriter = createCsvWriter({
  path: "out.csv",
  header: [
    { id: "sentence", title: "Sentence" },
    { id: "label", title: "Label" }
  ],
});

const data = [];
data.push({
  sentence: generatedRandomQuery,
  label: "0",
});
csvWriter
  .writeRecords(data)
  .then(() => console.log("The CSV file was written successfully"));
