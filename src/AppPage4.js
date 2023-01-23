function AppPage4() {
    return (
        <div className="body_1">
            <header>
                <nav className="navbar_nav">
                    <div className="icon_img">
                        <div className="hmbrgr_icon">
                            <span />
                            <span />
                            <span />
                        </div>
                        <img className="logo" src="./img/logo.png" alt="" />
                    </div>
                    <div className="btn_img">
                        <a className="user_img" href="#"><span>USER NAME</span><img src="./img/user_icon.png" alt="" /></a>
                    </div>
                </nav>
            </header>
            <main className="main_3">
                <h3>RULES OF THE MIND GAME</h3>
                {/* <p class="one_p"></p> */}
                <p>
                    All players form a single team. In the first round (level 1) each player receives 1 card, in the second round (level 2) they receive 2 cards, and so on.
                    <br /><br />
                    At each level the team members must put down all their cards in increasing order in the center of the table on an open stack, one after the other. For example (4 players, level 1): 18-34-41-73. The players do not take turns in any particular order.
                    <br /><br />
                    Whoever wants to put down a card, simply does so. Watch out, here's where it gets interesting: the players must not disclose anything about their own cards - no sharing of information, no secret signals
                    <br /><br />
                    The Mind is a game of synchronization which relies on your sense of time. The lower a card is, the earlier it will be played. A 5 would be played pretty swiftly, whereas an 80 is likely to be held in the player's hand for a while.
                    <br /><br />
                    Over the course of the game, the players become increasingly synchronized in terms of their sense of time, so they get better and better at estimating how much time needs to pass before playing a particular number card. What appears initially to be pure luck, becomes a real "skill" after playing for a while.
                    <br /><br />
                    So, to concentrate at the start of each level it might be more appropriate to say: "We're getting in synch!" It should be emphasized at this point that this is not a question of counting off the seconds.
                    There is no counting. Of course, time passes by "in the head" of each player, but this is normally quicker than one second per number and it changes depending on what level is being played.
                    <br /><br />
                    The secret of the game is developing that collective feeling for "now is the moment". The team has to work in harmony. The team must become ONE!!
                </p>
                <button>more info</button>
            </main>
            <footer>
                <a href>ABOUT US</a>
            </footer>
            <div className="user_profile">
                <div className="usr_usr_name">
                    <div className="close_menu">
                        <span />
                        <span />
                    </div>
                    <img src="./img/user_icon.png" alt="" />
                    <p>USER NAME</p>
                </div>
                <div className="statistics">
                    <p>statistics</p>
                    <div>
                        <span className="st-text">Played games:</span>
                        <span className="score">0</span>
                    </div>
                    <div>
                        <span className="st-text">Won games:</span>
                        <span className="score">0</span>
                    </div>
                    <div>
                        <span className="st-text">Played rounds:</span>
                        <span className="score">0</span>
                    </div>
                    <div>
                        <span className="st-text">Won rounds:</span>
                        <span className="score">0</span>
                    </div>
                    <div>
                        <span className="st-text">Score:</span>
                        <span className="score">0</span>
                    </div>
                </div>
                <div className="logout">
                    <button className="logout_btn">Log out</button>
                </div>
            </div>
        </div>
    );
}

export default AppPage4;
