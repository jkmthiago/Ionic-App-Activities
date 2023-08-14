document.addEventListener("DOMContentLoaded", async()=>{
    document.getElementById("btnGenerateFact").addEventListener("click", async()=>{
        getCatFact();
        document.getElementById("clickHereText").innerText = "Click the button bellow to see some more cat facts";
    })
})

async function getCatFact(){
    let result = await fetch("https://catfact.ninja/fact");
    let data = await result.json();
    document.getElementById("catFactText").innerText = data.fact;
}