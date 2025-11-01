-- Synthetic mobility schema
CREATE TABLE events (
  user_id INT,
  station_id INT,
  ts TIMESTAMP,
  clicks_1h INT,
  clicks_24h INT,
  purchases_7d INT,
  y INT
);
