package com.sai.aqe;
import org.springframework.web.bind.annotation.*;
import java.util.*;


@RestController
public class CardsController {
    static class Card { public String id; public String holder; public int limit; }
    private final Map<String, Card> store = new HashMap<>();


    @GetMapping("/cards")
    public Collection<Card> list(){ return store.values(); }


    @PostMapping("/cards")
    public Card create(@RequestBody Card in){
        Card c = new Card();
        c.id = UUID.randomUUID().toString();
        c.holder = in.holder; c.limit = in.limit;
        store.put(c.id, c);
        return c;
    }


    @PatchMapping("/cards/{id}/limit")
    public Card limit(@PathVariable String id, @RequestBody Map<String,Integer> body){
        Card c = store.get(id); if (c==null) throw new RuntimeException("not found");
        c.limit = body.getOrDefault("limit", c.limit); return c;
    }
}