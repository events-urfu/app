import React from "react";

function Header(){
    return (
        <header>
            <div className="wrapper">
                <div className="container-signin">
                    <ul>
                        <li className="logo"><a href="main.html"><img alt="#" className="pic-logo" src="/logo_1.png"/></a></li>
                        <li><img alt='#' className='pic-search' src="/search.png"/><input className="search" placeholder="Поиск по мероприятиям"/></li>
                        <li className="sign-in"><a href="/#">Вход</a></li>
                    </ul>
                </div>
            </div>
        </header>
    )
}

export default Header;