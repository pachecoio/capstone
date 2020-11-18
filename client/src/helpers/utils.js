export const DEFAULT_DATE_OPTIONS = {
  year: "numeric",
  month: "long",
  day: "numeric",
};

export const DEFAULT_DATE_LOCALE = "en-US";

export const getFormattedDate = (date) => {
  return new Date(date).toLocaleDateString(
    DEFAULT_DATE_LOCALE,
    DEFAULT_DATE_OPTIONS
  );
};

export const getFormattedTime = (date) => {
  const d = new Date(date);
  const hours = d.getHours();
  const minutes = d.getMinutes() < 10 ? `0${d.getMinutes()}` : d.getMinutes();
  return `${hours}:${minutes}`;
};

export const getShortDateTime = (date) => {
  const today = new Date();
  const d = new Date(date);
  const time = getFormattedTime(date);
  if (
    d.getDate() == today.getDate() &&
    d.getMonth() === today.getMonth() &&
    d.getFullYear() === today.getFullYear()
  ) {
    return `Today, ${time}`;
  }

  return `${d.getMonth()} ${d.getDate()} ${time}`;
};
