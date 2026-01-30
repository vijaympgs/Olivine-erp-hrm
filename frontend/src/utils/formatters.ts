export const formatCurrency = (value: number, currency = "INR") =>
  new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency
  }).format(value);

export const formatNumber = (value: number) =>
  new Intl.NumberFormat("en-IN").format(value);

