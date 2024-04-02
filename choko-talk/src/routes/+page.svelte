
<script>
    import { onMount } from 'svelte';
    import Message from '../Message.svelte';

    let ws;
    let user = "guest";
    let content = "";

    onMount(() => {
        ws = new WebSocket("ws://localhost:8000");

        ws.onmessage = (e) => {
            const data = JSON.parse(e.data);
            add_message(data.user, data.content, data.owner);
        };
    });

    function send_message(e) {
        if (e.key == "Enter") {
            ws.send(JSON.stringify({
                user: user,
                content: content,
            }));
            content = "";
        }
    }

    function add_message(recv_user, recv_content) {
        const chat_layout = document.querySelector(".chat-area");
        const element = new Message({
        target: chat_layout,
        props: {
            user: recv_user,
            content: recv_content,
            owner: user
        }
        });
    }
</script>

<svelte:head>
    <style>
        @import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css");

        html, body {
            height: 100vh;
            margin: 0;
            background: #b5cade;
            overflow: hidden;

            font-family: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif;
        }
    </style>
</svelte:head>

<style>
    .container {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .chat-area {
        padding: 2rem 1rem;
        height: calc(100% - 4rem);
        display: flex;
        flex-direction: column;
    }

    .input-area {
        height: 4rem;
        display: flex;
        flex-direction: row;
    }

    .user-name,
    .user-chat {
        font-size: 1.5rem;
        padding: 0.5rem 1rem;
        outline: none;
    }

    .input-area .user-name {
        width: 4rem;
        border-right: solid 1px #000;
        text-align: center;
    }

    .input-area .user-chat {
        width: calc(100% - 10rem);
        border: none;
    }

    button {
        width: 6rem;
        font-size: 1.5rem;
        border: none;
        background: #f7e111;
        color: #000000;
        font-weight: 700;
    }
</style>


<div class="container">
    <div class="chat-area"></div>

    <div class="input-area">
        <input bind:value={user} type="text" class="user-name">
        <input bind:value={content} on:keydown={send_message} type="text" class="user-chat">
        <button on:click={send_message}>전송</button>
    </div>
</div>