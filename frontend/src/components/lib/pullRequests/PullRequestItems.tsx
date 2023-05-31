import React from "react";
import { headerType } from "../../../types";
import PullRequestItem from "./PullRequestItem";

import style from "./PullRequestItems.module.scss";
import Card from "../../UI/card/Card";

const pullRequestDetails = [
  {
    id: "1",
    state: "open",
    title: "_",
    username: "roi",
    userAvatarUrl: "https://avatars.githubusercontent.com/u/64132493?v=4",
    times: {
      create: new Date(),
      update: new Date(),
      close: new Date(),
    },
    screenshotUrl:
      "https://storage.googleapis.com/github-monitor-integration.appspot.com/screenshots/pull_requests/1685537266.533633.png",
  },
  {
    id: "2",
    state: "open",
    title: "_",
    username: "roi",
    userAvatarUrl: "https://avatars.githubusercontent.com/u/64132493?v=4",
    times: {
      create: new Date(),
      update: new Date(),
      close: new Date(),
    },
    screenshotUrl:
      "https://storage.googleapis.com/github-monitor-integration.appspot.com/screenshots/pull_requests/1685537266.533633.png",
  },
  {
    id: "3",
    state: "open",
    title: "_",
    username: "roi",
    userAvatarUrl: "https://avatars.githubusercontent.com/u/64132493?v=4",
    times: {
      create: new Date(),
      update: new Date(),
      close: new Date(),
    },
    screenshotUrl:
      "https://storage.googleapis.com/github-monitor-integration.appspot.com/screenshots/pull_requests/1685537266.533633.png",
  },
];

function PullRequestItems() {
  return (
    <ul>
      {pullRequestDetails.map((detail) => {
        return (
          <li key={detail.id} className={style.prlist}>
            <Card>
              <PullRequestItem {...detail} />
            </Card>
          </li>
        );
      })}
    </ul>
  );
}

export default PullRequestItems;
