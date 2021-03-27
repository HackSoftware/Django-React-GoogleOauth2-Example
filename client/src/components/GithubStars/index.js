import GitHubButton from 'react-github-btn';
import classnames from 'classnames';

import styles from './GithubStars.module.css';

const GithubStars = ({ className }) => (
  <div className={classnames(styles.wrapper, className)}>
    <h4 className={styles.header}>You can star us on GitHub</h4>
    <GitHubButton
      className={styles.btnWrapper}
      href="https://github.com/HackSoftware/Django-React-GoogleOauth2-Example"
      data-icon="octicon-star"
      data-size="large"
      data-show-count="true"
      aria-label="Star our project on GitHub">
      Star
    </GitHubButton>
  </div>
);

export default GithubStars;
