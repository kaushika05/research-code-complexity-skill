classify_measurement <- function(value, group, include_missing = FALSE) {
  if (is.na(value)) {
    if (include_missing) return("missing")
    return(NA_character_)
  }
  if (group == "control") {
    if (value < 0) return("invalid")
    if (value > 10) return("high")
    return("typical")
  }
  if (group == "treatment") {
    if (value > 12) return("high")
    return("typical")
  }
  stop("unknown group")
}
