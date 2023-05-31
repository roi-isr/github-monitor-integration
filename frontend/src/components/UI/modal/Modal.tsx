import React, { MouseEventHandler } from "react";
import { createPortal } from "react-dom";
import { layoutType } from "../../../types";

import style from "./Modal.module.scss";
import Card from "../card/Card";

function Layout({
  children,
  closeHandler,
}: {
  children: JSX.Element;
  closeHandler: Function;
}) {
  return createPortal(
    <div className={style.modal} onClick={closeHandler as MouseEventHandler}>
      <Card>{children}</Card>
    </div>,
    document.getElementById("modal") as HTMLElement
  );
}

export default Layout;
