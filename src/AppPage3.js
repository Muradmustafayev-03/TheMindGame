function AppPage3() {
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
            <main className="main_2">
                <form>
                    <div className="sign_btns">
                        <button id="btnSign" className="sign-in">SIGN IN</button>
                        <button id="btnSignUp" className="sign-up active_btn">SIGN UP</button>
                    </div>
                    <input type="text" placeholder="username" />
                    <input id="nickname" className="nickname" type="text" placeholder="nickname" />
                    <input type="password" placeholder="password" className="pass_input" />
                    <div className="checkbox_div">
                        <input className="check" type="checkbox" />
                        <label htmlFor>Show password</label>
                    </div>
                    <button className="login_btn"><a href>SIGN UP</a></button>
                </form>
            </main>
            <footer>
                <a href="#">ABOUT US</a>
            </footer>
        </div>
    );
}

export default AppPage3;
