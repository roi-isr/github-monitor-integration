import React from "react";
import { layoutType } from "../../../types";

import style from "./Card.module.scss";

function Card({ children }: layoutType) {
  return <div className={style.card}>{children}</div>;
}

export default Card;
