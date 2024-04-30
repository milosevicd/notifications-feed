function addNotificationRows(jsonData, table) {
    jsonData.forEach(post => {
        if (post.comments && post.comments.length > 0) {
            let row = table.insertRow();
            let cell1 = row.insertCell();
            let cell2 = row.insertCell();

            // add avatar of the first user who commented
            if (post.comments[0].user.avatar) {
                let img = createAvatar(post.comments[0].user.avatar);
                cell1.appendChild(img);
            }

            // get a list of users who commented
            let users = post.comments.map(comment => comment.user);
            let usersText = formatUsers(users);
            cell2.innerHTML = `${usersText} commented on your post <b>"${post.content}"</b>`;
        }

        if (post.likes && post.likes.length > 0) {
            let row = table.insertRow();
            let cell1 = row.insertCell();
            let cell2 = row.insertCell();

            // add avatar of the first user who liked the post
            if (post.likes[0].user.avatar) {
                let img = createAvatar(post.likes[0].user.avatar);
                cell1.appendChild(img);
            }

            // get a list of users who liked the post
            let users = post.likes.map(like => like.user);
            let usersText = formatUsers(users);
            cell2.innerHTML = `${usersText} liked your post <b>"${post.content}"</b>`;
        }
    });
}

function createAvatar(avatar) {
    let img = document.createElement('img');
    img.classList.add('avatar');
    img.src = 'data:image/png;base64,' + avatar;
    return img;
}

function createLink(user) {
    // create a link to the user's profile page
    return `<a href="/user.html?user_id=${user.id}"><b>${user.name}</b></a>`;
}

function formatUsers(users) {
    // remove duplicate users
    users = users.filter((user, index, self) => self.findIndex(u => u.id === user.id) === index);

    // add a placeholder name for users without a name
    users = users.map(user => {
        if (!user.name) {
            return { ...user, name: '&lt;Anonymous User&gt;' };
        }
        return user;
    });

    // format users list, e.g. "Alice and Bob", "Alice, Bob and 2 others"
    if (users.length <= 2) {
        return users.map(user => createLink(user)).join(' and ');
    } else {
        let othersText = users.length - 2 === 1 ? 'other' : 'others';
        return `${createLink(users[0])}, ${createLink(users[1])} and ${users.length - 2} ${othersText}`;
    }
}