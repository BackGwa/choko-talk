<script>
    export let user = "";
    export let content = "";
    export let owner = "";
    let chat_class = owner == user ? "my-chat" : "other-chat";
</script>

<style>
    .my-chat, .other-chat {
        width: fit-content;
        padding: 0.75rem 1rem;
        margin-top: 2rem;
        border-radius: 0.5rem;
    }

    .my-chat {
        background: #f7e111;
    }

    .other-chat {
        background: #FFFFFF;
    }

    .user-name {
        position: absolute;
        margin-top: -2rem;
        margin-left: -1rem;
        font-size: 1rem;
        font-weight: 500;
    }
</style>

<div class={chat_class}>
    <div class="user-name">{user}</div>
    {content}
</div>