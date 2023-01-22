function AppPage2() {
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
                        <a className="user_img" href><span>USER NAME</span><img src="./img/user_icon.png" alt="" /></a>
                    </div>
                </nav>
            </header>
            <main className="main_1">
                <div className="main_1_div">
                    <img src="./img/img_2.png" alt="" />
                    <div className="buttons">
                        <button className="sign_in_up_btn"><a href>START</a></button>
                        <button className="rules_btn"><a href="./page4">RULES</a></button>
                    </div>
                </div>
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

export default AppPage2;
