const url = (appId) => `https://sellercentral.amazon.com/apps/authorize/consent?application_id=${appId}&version=beta&state=stateexample`

const link = (link) => {
    const el = document.createElement('a');
    el.href = link;
    el.target = '_blank';
    el.click();
}

const element = document.getElementById('amzn-btn');

element.addEventListener('click', (e) => link(url(e.currentTarget.getAttribute('data-appId'))));
