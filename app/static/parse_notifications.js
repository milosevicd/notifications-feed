function addNotificationRows(jsonData, table) {
    jsonData.forEach(post => {
        if (post.comments && post.comments.length > 0) {
            const row = table.insertRow();
            const cell1 = row.insertCell();
            const cell2 = row.insertCell();

            // add avatar of the first user who commented
            const img = createAvatar(post.comments[0].user.avatar);
            cell1.appendChild(img);

            // get a list of users who commented
            const users = post.comments.map(comment => comment.user);
            const usersText = formatUsers(users);
            cell2.innerHTML = `${usersText} commented on your post <b>"${post.content}"</b>`;
        }

        if (post.likes && post.likes.length > 0) {
            const row = table.insertRow();
            const cell1 = row.insertCell();
            const cell2 = row.insertCell();

            // add avatar of the first user who liked the post
            const img = createAvatar(post.likes[0].user.avatar);
            cell1.appendChild(img);

            // get a list of users who liked the post
            const users = post.likes.map(like => like.user);
            const usersText = formatUsers(users);
            cell2.innerHTML = `${usersText} liked your post <b>"${post.content}"</b>`;
        }
    });
}

function createAvatar(avatar) {
    const img = document.createElement('img');
    img.classList.add('avatar');
    img.src = 'data:image/png;base64,' + avatar;
    return img;
}

function createLink(user) {
    // create a link to the user's profile page
    return `<a href="/user.html?user_id=${user.id}"><b>${user.name}</b></a>`;
}

// format users list, e.g. "Alice and Bob", "Alice, Bob and 2 others"
function formatUsers(inputUsers) {
    let users = [...inputUsers];

    // remove duplicate users
    const uniqueUserIds = new Set(users.map(user => user.id));
    users = users.filter(user => uniqueUserIds.has(user.id));

    // add a placeholder name for users without a name
    users = users.map(user => {
        if (!user.name) {
            return { ...user, name: 'Unknown User' };
        }
        return user;
    });

    if (users.length <= 2) {
        return users.map(user => createLink(user)).join(' and ');
    } else {
        const othersText = users.length - 2 === 1 ? 'other' : 'others';
        return `${createLink(users[0])}, ${createLink(users[1])} and ${users.length - 2} ${othersText}`;
    }
}