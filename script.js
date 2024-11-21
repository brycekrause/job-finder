// https://jobdataapi.com/
const api_url = `https://jobdataapi.com/jobs`;

async function getJobs(){
    const response = await fetch(api_url);
    const data = response.json();
    document.writeln(data.results);
}