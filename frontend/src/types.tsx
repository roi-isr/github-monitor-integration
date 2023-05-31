export type headerType = {
  title: string;
  image_url?: string;
};

export type layoutType = {
  children: JSX.Element | JSX.Element[];
};

export type pullRequestItemType = {
  state: string;
  title: string;
  username: string;
  userAvatarUrl: string;
  screenshotUrl: string;
  times: {
    create: Date;
    update: Date;
    close: Date;
  };
};
