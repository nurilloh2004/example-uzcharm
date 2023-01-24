const tabs = document.querySelectorAll(".list-group-item"),
    tabsItems = document.querySelectorAll(".items"),
    tabsParent = document.querySelector(".list-group");

function hideTabContent() {
    tabsItems.forEach((item) => {
        item.classList.add("hide");
        item.classList.remove("show", "fade");
    });

    tabs.forEach((item) => {
        item.classList.remove("item_active");
    });
}

function showTabContent(i = 0) {
    tabsItems[i].classList.add("show", "fade");
    tabsItems[i].classList.remove("hide");

    tabs[i].classList.add("item_active");
}

hideTabContent();
showTabContent();
tabsParent.addEventListener("click", (e) => {
    e.preventDefault();
    const target = e.target;
    if (target && target.classList.contains("list-group-item")) {
        tabs.forEach((item, n) => {
            if (target == item) {
                hideTabContent();
                showTabContent(n);
            }
        });
    }
});