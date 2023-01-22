function App() {
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
            <button className="sgn_in_btn"><a href="./page3">SIGN IN/UP</a></button>
            <a className="user_img" href><img src="./img/user_icon.png" alt="" /></a>
          </div>
        </nav>
      </header>
      <main className="main_1">
        <div className="main_1_div">
          <img src="./img/img_2.png" alt="" />
          <div className="buttons">
            <button className="sign_in_up_btn"><a href="./page3">SIGN IN/UP</a></button>
            <button className="rules_btn"><a href="./page4">RULES</a></button>
          </div>
        </div>
      </main>
      <footer>
        <a href>ABOUT US</a>
      </footer>
    </div>
  );
}

export default App;
