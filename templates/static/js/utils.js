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

$(document).ready(() => {
  /*Fetch All Polls On Document Ready */
  if (window.location.href.includes("/demo/")) {
    const query = window.location.search;
    getRequest(`/api/polls/${query}`, renderPolls);
  }
});
