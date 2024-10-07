/*Utility Scripts */
function fetchGetRequest() {
  /*Fetch Every Get Request */
  const getRequestInputValue = document.getElementById("getRequestInput").value;
  const url = getRequestInputValue ? getRequestInputValue : "/api/polls/";
  getRequest(url, handleDemoRequest);
}
function handleDemoRequest(content) {
  /*Handle Live Demo */
  const sampleGetRequest = document.getElementById("sampleGetRequest");
  sampleGetRequest.innerHTML = JSON.stringify(content, null, 4);
}
