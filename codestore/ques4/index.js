//part A
// would first fetch the data 
// save into json Format


// onsubmit
//app.post("/", (req, res) =>{
    
//})
async function getData() {
  console.log("Fetching data... please wait.");
  
  try {
    // 1. Get the data from the URL
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    
    const users = await response.json();
   
    console.log("Success! Here are the users:");
    users.forEach(user => {
      console.log("- " + user.name);
    });

  } catch (error) {
    console.error("Something went wrong:", error);
  }
}

getData();

