/*Demo Project */

function renderPolls(content) {
  /*Render Polls in Content */
  const pollsItems = document.getElementById("pollsItems");
  loadPagination(content);
  if (content.count > 0) {
    content.results.forEach((elem) => {
      pollsItems.innerHTML += `  <div class="card card-side bg-base-100 shadow-xl border  hover:bg-base-200">
      <figure>
      <a  href="/api/polls/${elem.id}/">
            <img src="${elem.image}" class="w-40" alt="Movie" />
            </a>
            </figure>
        <div class="card-body">
            <h2 class="card-title">${elem.title}</h2>
            <p class="grid grid-cols-2 gap-4 items-center" id="poll_${elem.id}">
            </p>
        </div>
    </div>  `;
      updateChoices(`poll_${elem.id}`, elem, elem.choices);
    });
  } else {
    productsItems.parentElement.innerHTML = `<div role="alert" class="alert justify-center my-10">
 <i class="fa fa-info-circle"></i>
  <span>No Products Available else Check Console for API Error & Reach API Owner</span>
</div>`;
  }
}

function updateChoices(id, elem, choices) {
  let poll = document.getElementById(`${id}`);
  poll.innerHTML = "";
  choices.forEach((choice) => {
    poll.innerHTML += `<progress class="progress progress-primary h-4" value="${choice.votes}" max='${elem.get_total_votes}' onclick="vote('/api/polls/${elem.id}/?vote=${choice.id}')"></progress>`;
  });
}

/*Handle Pagination */
function loadPagination(content) {
  const previousBtn = document.getElementById("previousBtn");
  const nextBtn = document.getElementById("nextBtn");
  if (content.previous) {
    previousBtn.href =
      content.previous.split("/")[content.previous.split("/").length - 1];
  } else {
    previousBtn.href = window.location.search;
  }
  if (content.next) {
    nextBtn.href = content.next.split("/")[content.next.split("/").length - 1];
  } else {
    nextBtn.setAttribute("disabled", true);
    nextBtn.href = window.location.search;
  }
}

/*Filter Data */
function filterData() {
  const sortSelect = document.getElementById("sortSelect").value;
  window.location.search = `?page=1&orderby=${sortSelect}`;
}

/*Vote */
function vote(url) {
  patchRequest(url, null, voteUpdate);
}

function voteUpdate(content) {
  // console.log(content);
  updateChoices(`poll_${content.id}`, content, content.choices);
}
