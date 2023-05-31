import React from "react";
import { layoutType } from "../../../types";

import style from "./Layout.module.scss";

function Layout({ children }: layoutType) {
  return <div className={style.layout}>{children}</div>;
}

export default Layout;
