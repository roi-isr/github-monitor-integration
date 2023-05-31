import React, { useState } from "react";
import { pullRequestItemType } from "../../../types";
import Modal from "../../UI/modal/Modal";

import style from "./PullRequestItem.module.scss";

function PullRequestItem(props: pullRequestItemType) {
  const [showModal, setShowModal] = useState(false);
  return (
    <div className={style.pritem}>
      <section className={style.userDetails}>
        <img
          className={style.avatar}
          src={props.userAvatarUrl}
          alt={props.username}
        />
        <h1 className={style.username}>{props.username}</h1>
      </section>
      <hr></hr>
      <h2>PR Details</h2>
      <section className={style.prdetails}>
        <h3>State: {props.state}</h3>
        <h3>Title: {props.title}</h3>
      </section>
      <section className={style.prtimes}>
        <span>Created: {props.times.close.toDateString()}</span>
        <span>Updated: {props.times.update.toDateString()}</span>
        <span>Closed: {props.times.close.toDateString()}</span>
      </section>
      <a
        onClick={() => setShowModal(true)}
        className={style.screenshotLink}
        href="#"
      >
        Show screenshot
      </a>
      {showModal && (
        <Modal closeHandler={() => setShowModal(false)}>
          <img src={props.screenshotUrl} alt="Pull Request screenshot" />
        </Modal>
      )}
    </div>
  );
}

export default PullRequestItem;
