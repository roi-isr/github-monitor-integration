import React from "react";
import { headerType } from "../../../types";

import style from "./Header.module.scss";

function Header({ title, image_url }: headerType) {
  return (
    <div className={style.wrapper}>
      {image_url && <img alt="" className={style.image} src={image_url}></img>}
      <h1 className={style.title}>{title}</h1>
    </div>
  );
}

export default Header;
