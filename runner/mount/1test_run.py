import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://menzis.testsc.otap.menzis.nl/")
    page.get_by_role("button", name="Accepteren").dblclick()
    page.get_by_label("Knop gebruikers menu").dblclick()
    page.get_by_role("button", name="Loginstub", exact=True).dblclick()
    page.get_by_placeholder("BSN").dblclick()
    page.get_by_placeholder("BSN").fill("2698116229")
    page.get_by_role("button", name="Verzekerdennummer").dblclick()
    page.get_by_label("Knop gebruikers menu").dblclick()
    page.get_by_role("link", name="Mijn geldzaken").dblclick()
    page.get_by_role("button", name="1e herinnering 03-02-2024").dblclick()
    page.goto("https://menzis.testsc.otap.menzis.nl/mijn/geldzaken/betalingsregelingen/betalingsregeling-aanvragen")
    page.get_by_text("03-02-2024Eigen risico / eigen bijdrageTotaal€").dblclick()
    page.locator("div").filter(has_text=re.compile(r"^Eigen risico / eigen bijdrage$")).dblclick()
    page.get_by_role("button", name="Maandlasten bepalen").dblclick()
    page.get_by_label("Ik wil € 303,31 terugbetalen").select_option("6")
    page.get_by_label("Op elke").select_option("28")
    page.locator("label").filter(has_text="Ik ga akkoord met betaling").locator("span").first.click()
    page.get_by_role("button", name="Betalingsregeling aanvragen").dblclick()
    
    #transactie afkeuren
    page1.goto("chrome://newtab/")
    page1.goto("https://stichtingmenzisbeheer.sharepoint.com/:x:/r/sites/iv-classic/commercie/teamweb/_layouts/15/doc2.aspx?sourcedoc=%7BFDF1B099-FCBD-4ABA-B289-1F91C5F07278%7D&file=Web%20applicaties%20test-acc.xlsx&action=default&mobileredirect=true")
    page2.goto("http://intranetapplications.test.otap.loods2.org/TransactionService.Pres.Internal/Default.aspx")
    page2.get_by_role("link", name="Transacties").dblclick()
    page2.frame_locator("iframe[name=\"frContent\"]").get_by_role("link", name="Status").dblclick()
    page2.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_text("wacht op autorisatie").dblclick()
    page2.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").locator("#ddlTransactieType_dropDownList").select_option("4157")
    page2.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("button", name="ZOEKEN").dblclick()
    page2.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("cell", name="Aanvraag betalingsregeling DERI BO", exact=True).dblclick()
    page2.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("link", name="478133").dblclick()
    page2.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("button", name="Toe-eigenen").dblclick()
    page2.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("button", name="Afkeuren").dblclick()
